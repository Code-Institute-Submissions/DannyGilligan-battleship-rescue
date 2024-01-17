# Battleship Rescue

![Hero Image](assets/documentation/battleship_rescue_hero_image.webp)
<br>
<br>
<br>

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Design](#design)
* [User Stories](#user-stories)
* [Bugs](#bugs)
* [Manual Testing](#manual-testing)
* [Deployment](#deployment)
* [Technologies Used](#technologies-used)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)
<br>
<br>
<br>


## Introduction
<br>
<br>
<br>

## Features
<br>
<br>
<br>

## Design

An overview of the key design aspects of the project is included below.

<details> <!-- Container for process flows starts here -->
  <summary><b>Process Flows</b></summary>
<br>
The diagrams below represent the process flows throughout the main phases of the game (these are best viewed in raw format).
<br>
<br>
<details>
  <summary><i> Phase 1: Initialise Game</i></summary>
<br>

![Phase 1](assets/documentation/01_initialise_game.webp)
</details>

<details>
  <summary><i> Phase 2: User Shot</i></summary>
<br>

![Phase 2](assets/documentation/02_user_shot.webp)
</details>

<details>
  <summary><i> Phase 3: Enemy Shot</i></summary>
<br>

![Phase 3](assets/documentation/03_enemy_shot.webp)
</details>

<details>
  <summary><i> Phase 4: End Game</i></summary>
<br>

![Phase 3](assets/documentation/04_end_game_conditions.webp)
</details>

</details> <!-- Container for process flows ends here -->
<br>
<br>
<br>

## User Stories
<br>
<br>
<br>

## Bugs
<br>
<br>
<br>

## Manual Testing
<br>
<br>
<br>

## Deployment
<br>
<br>
<br>

## Technologies Used
<br>
<br>
<br>

## Credits

<details>
  <summary>Reference Materials Used</summary>
<br>

<table>
<tr><th><b> Description </b></th><th><b> Link </b></th></tr>
<!-- Reference Material 1 begins -->
<tr><td> Code Institute README.md Tutorial by Kasia Bogucka </td>
<td> 

[here](https://www.youtube.com/watch?v=l1DE7L-4eKQ)  

</td></tr>
<!-- Reference Material 1 ends -->
<tr><td> Guide to Milestone 3 MVP by Kasia Bogucka </td>
<td> 

[here](https://www.youtube.com/watch?v=nNXmC6Tq0qw)  

</td></tr>
<!-- Spacer -->
<tr><td> Guide on code validation by Lane-Sawyer Thompson & Matt Rudge </td>
<td> 

[here](https://www.youtube.com/watch?v=wiqAvRCheKo)  

</td></tr>
<!-- Spacer -->
<tr><td> Milestone 3 Project FAQs by Lane-Sawyer Thompson & Lucy Rush </td>
<td> 

[here](https://www.youtube.com/watch?v=BDKvisxzEbk)  

</td></tr>
<!-- Spacer -->


</table>
<br>
<br>
<br>
</details>

<details>
  <summary>Images</summary>
<br>

<table>
<tr><th><b> Thumbnail </b></th><th><b> Production File Name </b></th><th><b> Description </b></th><th><b> Source </b></th></tr>
<!-- image 1 begins -->
<tr><td>

![Hero Image](assets/documentation/hero_image_thumbnail.webp)
</td>

<td>battleship-rescue-hero-image.webp</td>
<td>Hero image used for README.md</td>
<td>

[here](https://wall.alphacoders.com/big.php?i=652229)
</td>
</tr>



</table>




</details>


<br>
<br>
<br>

## Acknowledgements
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>








## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

