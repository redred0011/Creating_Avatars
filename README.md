Avatar Generation Program

This program allows you to generate avatars using the DiceBear Avatars API and save them to your local machine. You can choose between different options to generate and save avatars.

------Options------

1. Random Avatar and save in the main folder
This option generates a random avatar using the DiceBear Avatars API and saves it in the main folder where the program is located.

2. Choose Avatar and save in the main folder
This option allows you to choose a specific avatar style from [DiceBear Avatars styles](https://www.dicebear.com/styles) by entering the avatar number. The selected avatar will be saved in the main folder.

3. Random Avatar + Create new folder and save
This option generates a random avatar using the DiceBear Avatars API and allows you to create a new folder to save the avatar. If you choose not to enter a folder name, the avatar will be saved in a folder named "avatars" (default).

4. Choose Avatar + Create new folder and save
This option allows you to choose a specific avatar style from [DiceBear Avatars styles](https://www.dicebear.com/styles) by entering the avatar number. The selected avatar will be saved in a newly created folder named "avatars".

Notes
- The avatars are saved in SVG format.
- The program utilizes the `requests` library to make HTTP requests to the DiceBear Avatars API.
- The `pathlib` library is used for creating new folders and managing file paths.

Enjoy generating and saving avatars with this program!
