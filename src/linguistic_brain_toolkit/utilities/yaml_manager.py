import yaml
from typing import Any, Dict, Optional


class YamlManager:
    """
    Clase para gestionar archivos YAML.

    Esta clase proporciona métodos para cargar datos desde un archivo YAML y obtener
    valores específicos de los datos cargados.

    Attributes:
        file_path (str): Ruta del archivo YAML.
        data (Any): Datos YAML cargados.
    """
    def __init__(self, file_path: str):
        """
        Inicializa YamlManager con la ruta del archivo YAML.

        Args:
            file_path (str): Ruta del archivo YAML.
        """
        self.file_path = file_path
        self.data = self._load_yaml()

    def _load_yaml(self) -> Any:
        """
        Carga datos YAML desde un archivo.

        Returns:
            Any: Datos YAML parseados.

        Raises:
            FileNotFoundError: Si el archivo no existe.
            yaml.YAMLError: Si hay un error al analizar el YAML.
        """
        try:
            with open(self.file_path, "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.file_path}") from e
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML: {e}") from e

    def get_yaml(self, prompt: str) -> Dict[str, Any]:
        """
        Obtiene un valor específico de los datos YAML cargados.

        Args:
            prompt (str): Nombre del prompt en el archivo YAML (e.g., 'system_prompts').

        Returns:
            Dict[str, Any]: Diccionario que contiene el prompt especificado.

        Raises:
            KeyError: Si no se encuentra el prompt especificado.
        """
        try:
            return self.data.get(prompt, {})
        except KeyError as e:
            raise KeyError(f"Prompt '{prompt}' not found in the loaded data.") from e
