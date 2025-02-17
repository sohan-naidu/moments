# Instructions

Please create a Computer Vision instance in Azure [here](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryItemDetailsBladeNopdl/id/Microsoft.CognitiveServicesComputerVision/selectionMode~/false/resourceGroupId//resourceGroupLocation//dontDiscardJourney~/false/selectedMenuId/home/launchingContext~/%7B%22galleryItemId%22%3A%22Microsoft.CognitiveServicesComputerVision%22%2C%22source%22%3A%5B%22GalleryFeaturedMenuItemPart%22%2C%22VirtualizedTileDetails%22%5D%2C%22menuItemId%22%3A%22home%22%2C%22subMenuItemId%22%3A%22Search%20results%22%2C%22telemetryId%22%3A%22b205967c-15d1-4ea5-b073-9b345fde6376%22%7D/searchTelemetryId/2a76201f-0545-454b-8e60-27db7be54ad4)

Then update .env:

    AZURE_VISION_API_ENDPOINT = "<your-api-endpoint>"
    AZURE_VISION_API_KEY = "<your-api-token>"

Once a virtual environment has been created, run the following commands:

```
pip install -r requirements.txt
flask init-db
flask lorem
flask run
```

It will create a test account:

    email: admin@helloflask.com
    password: moments

This account can be used for testing both the features.
