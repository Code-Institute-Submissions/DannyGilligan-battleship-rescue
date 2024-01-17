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

The app was deployed as a Minimum Viable Product using the Heroku platform.

<details>
  <summary><b>The steps for deployment are outlined here</b></summary>
<br>

<!-- spacer -->
<details>
  <summary><i> Step 1: Create app</i></summary>
<br>
In the Heroku dashboard, populate the 'App name' field and choose a region. Then click on 'Create app'.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_1_create_app.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 2: App setup page</i></summary>
<br>
Once the app is created, the setup page will be displayed. This page contains an overview of the data related to the app. From here, navigate to the 'Settings' tab.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_2_app_setup_page.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>



</details>
<!-- spacer -->
<details>
  <summary><i> Step 3: Settings</i></summary>
<br>
On the Settings page, click on the 'Reveal Config Vars' button.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_3_settings.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>




</details>
<!-- spacer -->
<details>
  <summary><i> Step 4: Config vars</i></summary>
<br>
In the Config Vars, add 'PORT' and '8000' in the fields as shown below. Then click 'Add'.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_4_config_vars.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 5: Add buildpacks</i></summary>
<br>
Once the Config Vars are added, the next step is to add two buildpacks to the app. Scroll down to the Buildpacks section and click on the 'Add buildpack' button.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_5_add_buildpacks.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>


</details>
<!-- spacer -->
<details>
  <summary><i> Step 6: Add python buildpack</i></summary>
<br>
Select the python option from the menu, then click 'Add buildpack'. To note, it is important that the python buildpack is added first <b>before</b> any other buildpack!
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_6_add_python_buildpack.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 7: Add node.js buildpack</i></summary>
<br>
Once the python buildpack is added, select the node.js buildpack from the menu and click on the 'Add buildpack' button. To note, it is important that the node.js buildpack is added <b>after</b> the python buildpack!
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_7_add_nodejs_buildpack.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 8: Deploy screen</i></summary>
<br>
Once the buildpacks have been added (python, followed by node.js), navigate to the 'Deploy' tab.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_8_deploy_screen.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 9: Select Github</i></summary>
<br>
Select Github from the 'Deployment method' options.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_9_select_github.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>


</details>
<!-- spacer -->
<details>
  <summary><i> Step 10: Enter repository name</i></summary>
<br>
Enter the repository name in the 'Connect to Github' field as shown below, then click on the 'Seach' button.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_10_enter_repository.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 11: Connect</i></summary>
<br>
Once the repository has been located, click on the 'Connect' button.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_11_click_connect.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 12: Connection confirmation</i></summary>
<br>
A confirmation will be displayed on the Github once the repository is connected to the Heroku app as shown below.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_12_connected_confirmation.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 13: Enable automatic deploys (optional)</i></summary>
<br>
Automatic deploys can be enabled if so desired by clicking on the 'Enable Automatic Deploys' button, this will result in the app being refreshed with updated code every time changes are pushed to Github. 
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_13_enable_auto_deploys.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 14: Manual deployment</i></summary>
<br>
The initial deployment of the app can be triggered by selecting 'main' from the 'Choose a branch to deploy' menu, then clicking on the 'Deploy Branc' button.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_14_manual_deploy.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 15: Deployment confirmation</i></summary>
<br>
Once the app build and deployment has been completed in Heroku, a confirmation will be displayed as shown below. The app can now be viewed by clicking on the 'View' button.
<br>
The deployment process is now complete.
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_15_deployment_confirmation.webp)

</td>
<td>
:heavy_check_mark:
</td>
</table>

</details>
<!-- spacer -->

</details>



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

