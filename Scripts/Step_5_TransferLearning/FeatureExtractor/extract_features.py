# -*- coding: utf-8 -*-

import argparse
import csv
import os

import numpy as np
import tensorflow as tf

from networks.lenet import LeNet
from networks.pure_cnn import PureCnn
from networks.network_in_network import NetworkInNetwork
from networks.resnet import ResNet
from networks.densenet import DenseNet
from networks.wide_resnet import WideResNet
from networks.capsnet import CapsNet


class FileToImageConverter:
    """Converte o conteúdo completo de um arquivo em uma representação determinística de 32 x 32 x 3. Importante: Nenhum ruído ou componente aleatória é adicionada. O conteúdo completo do arquivo participa da representação. Arquivos maiores que 3072 bytes são redimensionados por interpolação linear, em vez de serem simplesmente truncados. Arquivos menores que 3072 bytes recebem padding com zero."""

    def __init__(self, target_size=(32, 32)):
        self.target_size = target_size
        self.target_bytes = target_size[0] * target_size[1] * 3

    def _process_file(self, file_path):
        """Lê o conteúdo completo do arquivo como sequência de bytes."""
        with open(file_path, "rb") as f:
            byte_content = f.read()
        if len(byte_content) == 0:
            raise ValueError(f"Arquivo vazio: {file_path}")
        return np.frombuffer(byte_content, dtype=np.uint8)

    def _resize_bytes(self, byte_array):
        """Redimensiona deterministicamente a sequência completa de bytes para o número de valores necessário à imagem. Nenhuma informação aleatória é introduzida."""
        if len(byte_array) == self.target_bytes:
            return byte_array.copy()
        if len(byte_array) < self.target_bytes:
            resized = np.zeros(self.target_bytes, dtype=np.uint8)
            resized[:len(byte_array)] = byte_array
            return resized
        x_original = np.linspace(0.0, 1.0, num=len(byte_array), endpoint=True)
        x_target = np.linspace(0.0, 1.0, num=self.target_bytes, endpoint=True)
        resized = np.interp(x_target, x_original, byte_array.astype(np.float32))
        return np.clip(resized, 0, 255).astype(np.uint8)

    def convert_to_image(self, file_path):
        """Converte o conteúdo completo do arquivo em uma imagem RGB de tamanho 32 x 32 x 3. Os 3072 valores correspondem diretamente à sequência de bytes redimensionada/padronizada, sem geração de informação aleatória."""
        byte_array = self._process_file(file_path)
        resized_bytes = self._resize_bytes(byte_array)
        image = resized_bytes.reshape(self.target_size[0], self.target_size[1], 3)
        if image.shape != (self.target_size[0], self.target_size[1], 3):
            raise ValueError(f"Dimensão inesperada para {file_path}: {image.shape}")
        return image


class CustomDatasetLoader:
    """Processa arquivos benignos e malware em streaming. O loader não mantém o dataset completo na memória durante a extração de características."""

    def __init__(self, benign_dir, malware_dir):
        self.converter = FileToImageConverter()
        self.benign_dir = benign_dir
        self.malware_dir = malware_dir
        self.class_names = ["benign", "malware"]

    def _iter_files(self):
        """Percorre os arquivos em ordem determinística. Retorna: class_name, file_path, filename"""
        for class_name, data_dir in [("benign", self.benign_dir), ("malware", self.malware_dir)]:
            if not os.path.isdir(data_dir):
                print(f"Warning: Directory '{data_dir}' does not exist. Skipping {class_name}.")
                continue
            filenames = sorted(filename for filename in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, filename)))
            print(f"Found {len(filenames)} files in {class_name} directory.")
            for filename in filenames:
                yield (class_name, os.path.join(data_dir, filename), filename)

    def save_as_libsvm_streaming(self, output_file, classifier):
        """Extrai características da CNN e salva em LIBSVM, processando uma amostra por vez."""
        out_dir = os.path.dirname(output_file)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        expected_num_features = None
        processed = 0
        errors = 0
        with open(output_file, "w", encoding="utf-8") as f:
            for class_name, file_path, filename in self._iter_files():
                label = 0 if class_name == "benign" else 1
                try:
                    image = self.converter.convert_to_image(file_path)
                    features = classifier.extract_features(image)[0]
                    features = np.asarray(features).reshape(-1)
                    if expected_num_features is None:
                        expected_num_features = len(features)
                    elif len(features) != expected_num_features:
                        raise ValueError(f"Número de características inconsistente: esperado {expected_num_features}, obtido {len(features)}.")
                    line = str(label)
                    for j, value in enumerate(features):
                        value = float(value)
                        if value != 0.0:
                            line += f" {j + 1}:{value:.6f}"
                    f.write(line + "\n")
                    processed += 1
                except Exception as e:
                    errors += 1
                    print(f"Erro ao processar {file_path}: {e}")
        print(f"LIBSVM salvo em: {output_file}")
        print(f"Amostras processadas: {processed} | Erros: {errors} | Características por amostra: {expected_num_features}")

    def save_as_csv_streaming(self, output_file, classifier, delimiter=";"):
        """Extrai características da CNN e salva em CSV, processando uma amostra por vez. O CSV contém: app;output;feature_1;feature_2;..."""
        out_dir = os.path.dirname(output_file)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        num_features = None
        processed = 0
        errors = 0
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=delimiter)
            for class_name, file_path, filename in self._iter_files():
                label = 0 if class_name == "benign" else 1
                try:
                    image = self.converter.convert_to_image(file_path)
                    features = classifier.extract_features(image)[0]
                    features = np.asarray(features).reshape(-1)
                    if num_features is None:
                        num_features = len(features)
                        header = ["app", "output"] + [f"feature_{i + 1}" for i in range(num_features)]
                        writer.writerow(header)
                    elif len(features) != num_features:
                        raise ValueError(f"Número de características inconsistente: esperado {num_features}, obtido {len(features)}.")
                    row = ([filename, label] + [f"{float(v):.6f}" for v in features]) #impedir notação cientifica row = ([filename, label] + [round(float(v), 6) for v in features]) -----------------------------------------
                    writer.writerow(row)
                    processed += 1
                except Exception as e:
                    errors += 1
                    print(f"Erro ao processar {file_path}: {e}")
        print(f"CSV salvo em: {output_file}")
        print(f"Amostras processadas: {processed} | Erros: {errors} | Características por amostra: {num_features}")


class Classifier:
    """Carrega uma das CNNs disponíveis e utiliza sua penúltima camada como extrator de características. A rede é carregada com os pesos indicados pela implementação correspondente. Este arquivo não realiza treinamento da CNN."""

    def __init__(self, model_name="lenet"):
        self.model_defs = {"lenet": LeNet, "pure_cnn": PureCnn, "net_in_net": NetworkInNetwork, "resnet": ResNet, "densenet": DenseNet, "wide_resnet": WideResNet, "capsnet": CapsNet}
        if model_name not in self.model_defs:
            raise ValueError(f"Model '{model_name}' not found. Available models: {list(self.model_defs.keys())}")
        self.model = self.model_defs[model_name](load_weights=True)
        self.class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
        self.feature_model = tf.keras.Model(inputs=self.model._model.input, outputs=self.model._model.layers[-2].output)
        self.feature_model.trainable = False

    def extract_features(self, image):
        """Extrai o vetor de características da penúltima camada. A normalização para [0, 1] deve ser compatível com o pré-processamento utilizado no treinamento original da CNN. Essa compatibilidade deve ser confirmada no arquivo da rede."""
        image = np.asarray(image)
        if image.ndim == 3:
            image = np.expand_dims(image, axis=0)
        if image.ndim != 4:
            raise ValueError(f"Entrada deve possuir 3 ou 4 dimensões. Shape recebido: {image.shape}")
        image = image.astype(np.float32) / 255.0
        features = self.feature_model.predict(image, verbose=0)
        return features


def main():
    parser = argparse.ArgumentParser(description="Extração de características de arquivos benignos e malware utilizando CNNs pré-treinadas.")
    parser.add_argument("-model", default="lenet", choices=["lenet", "resnet", "densenet", "wide_resnet", "capsnet"], help="CNN utilizada como extrator de características.")
    parser.add_argument("-data_benign", required=True, type=str, help="Diretório contendo arquivos benignos.")
    parser.add_argument("-data_malware", required=True, type=str, help="Diretório contendo arquivos de malware.")
    parser.add_argument("-libsvm_file", default="FeatureExtractor/TransferLearningAntivirus.libsvm", help="Arquivo de saída no formato LIBSVM.")
    parser.add_argument("-csv_file", default="FeatureExtractor/TransferLearningAntivirus.csv", help="Arquivo de saída no formato CSV.")
    args = parser.parse_args()

    if not os.path.isdir(args.data_benign):
        raise SystemExit(f"Error: Benign directory '{args.data_benign}' does not exist.")
    if not os.path.isdir(args.data_malware):
        raise SystemExit(f"Error: Malware directory '{args.data_malware}' does not exist.")

    os.makedirs("FeatureExtractor/networks/pretrained_weights", exist_ok=True)
    os.makedirs("FeatureExtractor/networks/results", exist_ok=True)

    print(f"\nInicializando modelo {args.model.upper()} para extração de características...")
    classifier = Classifier(args.model)
    loader = CustomDatasetLoader(args.data_benign, args.data_malware)

    print("\nProcessamento em streaming: um arquivo por vez.")
    #print(f"\nSalvando características em LIBSVM: {args.libsvm_file}")
    #loader.save_as_libsvm_streaming(args.libsvm_file, classifier)

    print(f"\nSalvando características em CSV: {args.csv_file}")
    loader.save_as_csv_streaming(args.csv_file, classifier, delimiter=";")

    print("\nProcesso concluído. As características foram extraídas pela penúltima camada da CNN.")


if __name__ == "__main__":
    main()
