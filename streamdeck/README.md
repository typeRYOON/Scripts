# Scripts
> This folder contains Stream Deck scripts that perform various tasks. You can use anything to launch these programs, a Stream Deck is simply for ease of use.
> Below are script descriptions, what they do, and what command to run it locally on your Stream Deck.
---
> [**Collapse.pyw - Folder Tree Collapser (for specified extension files)**](#collapse-- "Collapse")   
> This script collapses the folder structure within your downloads folder, recursively traverses subfolders, and moves files of a specified extension (default = image files) to a folder named "New". It handles multiple collapses gracefully, appending new folder contents to the end of the "New" folder. Any files not matching the specified extension are moved to "New\Else*".
>
> The collapse operation follows a preorder traversal, moving files as it encounters them during recursion. Once no more folders remain to traverse into, the script automatically deletes the collapsed folder. It also ensures not to extract archives that are currently being downloaded (checking for .part files).
> 
> Dependencies:
> - Requires 7zip for folder extraction. Modify the zipExtracter function if using a different extraction tool.
>
> Usage:
> Replace the following variables with your local paths:
> - DL: Download folder path
> - DLN: Expected new folder path
> - sZip: Path to your 7zip executable
---  
> ### Collapse : :  
---
