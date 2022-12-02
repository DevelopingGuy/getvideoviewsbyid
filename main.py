# Imports
from TikTokApi import TikTokApi
import sys

# Declare the API
api = TikTokApi()

# Get argument 1 from command line
idraw = sys.argv[1]

# Get the starts of the video binded with the ID given
id = api.video(id=idraw).stats

# Turn dictionary into variables
locals().update(id)

# Print the video views
print(playCount)
