<a name="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/typeRYOON/Scripts">
    <img src="resources/logo.ico" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Scripts</h3>

  <p align="center">
     Scripts I've created and maintain!
    <br />
    <a href="https://github.com/typeRYOON/Scripts/issues"><strong>Report Bug »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Stream Deck
> This folder contains Stream Deck scripts that perform various tasks. You can use anything to launch these programs, a Stream Deck is simply for ease of use.
> Below are script descriptions, what they do, and what command to run it locally on your Stream Deck.
---
> [**Collapse.pyw - Folder Tree Collapser (for specified extension files)**](https://github.com/typeRYOON/Scripts/blob/main/streamdeck/Collapse.pyw "Collapse")   
> This script collapses the folder structure within your downloads folder, recursively traverses subfolders, and moves files of a specified extension (default = image files) to a folder named "New". It handles multiple collapses gracefully, appending new folder contents to the end of the "New" folder. Any files not matching the specified extension are moved to "New\Else*".
>
> The collapse operation follows a preorder traversal, moving files as it encounters them during recursion. Once no more folders remain to traverse into, the script automatically deletes the collapsed folder. It also ensures not to extract archives that are currently being downloaded (checking for .part files).
> 
> Dependencies:
> - Requires 7zip for folder extraction. Modify the zipExtracter function if using a different extraction tool.
>
> Replace the following variables with your local paths:
> - DL: Download folder path
> - DLN: Expected new folder path
> - sZip: Path to your 7zip executable
> - Optional: Replace the tuples around line 26/28 with file extentions you'd like to specify. 
>
> Stream Deck Open Command:
> `pyw "$(PATH)\Collapse.pyw"`   
<p align="right">(<a href="#readme-top">back to top</a>)</p>

> [**EmptyRecycleBin.pyw - Empty Recycle Bin**](https://github.com/typeRYOON/Scripts/blob/main/streamdeck/EmptyRecycleBin.pyw "EmptyRecycleBin")  
> This script empties the recycle bin using winshell (Windows Python Module).
>
> Dependencies:   
> - `pip install winshell`
> 
> Stream Deck Open Command:
> `pyw "$(PATH)\EmptyRecycleBin.pyw"`
<p align="right">(<a href="#readme-top">back to top</a>)</p>
