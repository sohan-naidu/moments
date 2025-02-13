import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures

class AzureVision:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = ImageAnalysisClient(
                endpoint=os.getenv("AZURE_VISION_API_ENDPOINT"),
                credential=AzureKeyCredential(os.getenv("AZURE_VISION_API_KEY"))
            )
        return cls._instance

    def get_alt_text(self, image: bytes):
        result = self.client.analyze(
            image_data=image,
            visual_features=[VisualFeatures.CAPTION]
        )

        return result.caption.text if result.caption else ""
