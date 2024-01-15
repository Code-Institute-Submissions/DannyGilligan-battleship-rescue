# Battleship Rescue

![Hero Image](assets/documentation/battleship-rescue-hero-image.webp)

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

An overview of the key design aspects is included below.

<details> <!-- Container for process flows starts here -->
  <summary><b>Process Flows</b></summary>
<br>

<details>
  <summary><i> Phase 1: Initialise Game</i></summary>
<br>

![Phase 1](assets/documentation/01%20Initialise%20Game%20(cropped).webp)
</details>

<details>
  <summary><i> Phase 2: User Shot</i></summary>
<br>

![Phase 2](assets/documentation/02%20User%20Shot%20(cropped).webp)
</details>

<details>
  <summary><i> Phase 3: Enemy Shot</i></summary>
<br>

![Phase 3](assets/documentation/03%20Enemy%20Shot%20(cropped).webp)
</details>

<details>
  <summary><i> Phase 4: End Game</i></summary>
<br>

![Phase 3](assets/documentation/04%20End%20Game%20Conditions%20(cropped).webp)
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


</details>

<details>
  <summary>Images</summary>
<br>


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

