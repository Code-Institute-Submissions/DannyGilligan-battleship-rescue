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

<!------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ USER STORIES SECTION -->
## User Stories 

The user stories relating to this MVP version of the game, from the perspective of both a user and a developer, are outlined below.
<br>
<!-- 'As a user' User Stories are shown below -->
<details>
  <summary><b>As a User</b></summary>
<br>
<table>
<tr>
<th>User Story</th><th>Result</th>
</tr>
<!-- User Story 1 begins -->
<tr>
<td>I am presented with a clear, organised start screen with game logo</td><td>:heavy_check_mark:</td>
</tr>
<!-- User Story 1 ends -->
<tr>
<td>I can enter a username<td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If the username I submit is invalid, I am alerted to this and the requirements are emphasised to me</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am presented with difficulty levels to choose from</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If I enter an incorrect difficulty level, I am alerted to this and the requirements are emphasised to me</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am presented with a narrative providing a back story to the game and mission details</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can choose to accept or reject the mission</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If I enter the wrong input at the mission accept screen, I am alerted to this and the requirements are emphasised to me</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If I choose to reject the mission, I am provided with a confirmation message</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>When I choose to accept the mission, I am presented with a sitrep display providing details of the battleship</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am presented with a clear, organised game screen giving an overview of the information related to the battle</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see how many torpedos are remaining</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see how many hull plates are remaining</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see how many enemy ships are remaining</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see how many merchant ships are remaining</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see how many shot I've missed</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see my shot accuracy</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see how many enemy ships have been destroyed</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see how many merchant ships have been destroyed</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am presented with a clear, organised 'battle grid' with rows and columns clearly identified</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see the 'weapons ready' message</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see where to enter the input for the row to fire upon</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If I enter an incorrect row input, I am alerted to this and the requirements are emphasised to me</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can clearly see where to enter the input for the column to fire upon</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If I enter an incorrect column input, I am alerted to this and the requirements are emphasised to me</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with immediate feedback if my shot was a miss</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with immediate feedback if my shot destroyed an enemy ship</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with immediate feedback if my shot destroyed a merchant ship</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am alerted when the enemy is firing upon my battleship</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with immediate feedback if the enemy shot hit my battleship</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with immediate feedback if the enemy shot missed</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with a battle update and mission status overview upon failing the mission</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with a narrative when the mission fails</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with a battle update and mission status overview upon accomplishing the mission</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with a narrative when the mission succeeds</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can choose to restart the game from the end game screen</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I can choose to exit the game from the end game screen</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->

</table>

[Back to User Stories](#user-stories)
<br>
<br>
<br>

</details>
<!-- 'As a User' User Stories end here -->
<!-- 'As a Developer' User Stories are shown below -->
<details>
  <summary><b>As a Developer</b></summary>
<br>
<table>
<tr>
<th>User Story</th><th>Result</th>
</tr>
<!-- spacer -->
<tr>
<td>I am presented with a clean, organised repository to work with</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with docstrings and relevant comments in the run.py file</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with a clear, organised README.md file</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>I am provided with detailed instructions on the deployment steps</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
</table>

[Back to User Stories](#user-stories)
<br>
<br>
<br>

</details>
<!-- User Stories section ends here -->
<br>
<br>
<br>



## Bugs
<br>
<br>
<br>

## Manual Testing

Several manual tests were performed during playthroughs of the game. The results of which are outlined below.

<!-- Manual tests are shown below -->
<details>
  <summary><b>Manual Testing</b></summary>
<br>
<table>
<tr>
<th>Manual Test Scenario</th><th>Result</th>
</tr>
<!-- User Story 1 begins -->
<tr>
<td>Banner art displays correctly on start screen</td><td>:heavy_check_mark:</td>
</tr>
<!-- User Story 1 ends -->
<tr>
<td>Tag lines display correctly on start screen<td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>Enter call sign prompt, with requirements highlighted, displays correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>When call sign does not meet requirements, alert is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>Mission difficulty screen displays correctly, with options clearly visible</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>When incorrect mission difficulty option is entered, alert is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>Cadet, Captain and Admiral difficulty options are recognised and accepted as valid inputs</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>Connection to 'Central Command' animation displays correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>Back story and mission details screen is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>Prompt to accept mission, with input requirements clearly visible, is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If invalid input is entered for the accept mission prompt, alert is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If mission is rejected, message and confirmation is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>When mission is accepted, the sitrep module loading screen is displayed correctly </td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The sitrep display screen is then displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>All initial game values in the sitrep display are presented correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The battle grid is displayed correctly with default symbols and row and columns clearly identified</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The weapons ready message is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The input to accept row to fire upon is displayed correctly<td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If an invalid row input is entered, the alert is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The input to accept column to fire upon is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>If an invalid column input is entered, the alert is displayed correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The shot feedback animation displays correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The sitrep panel data updates correctly if the shot is a miss</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The sitrep panel data updates correctly if the shot is an enemy hit</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The sitrep panel data updates correctly if the shot is a merchant ship hit</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The sitep panel updates the shot accuracy percentage correctly after each user shot</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The enemy torpedo in the water alert displays correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The enemy shot feedback animation displays correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The sitrep panel updates correctly if the enemy shot hits the user's battleship</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The loop behaves as expected and requests another user shot after enemy shot is processed</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The battle grid is updated correctly with an 'X' symbol if the user shot misses</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The battle grid is updated correctly with an 'E' symbol if the user shot destroys an enemy ship</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The battle grid is updated correctly with an 'M' symbol if the user shot destroys an enemy ship</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The battle grid does not overwrite an 'E' or 'M' symbol with 'X' if user fires on same coordinates</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>All variations of shot inputs from row 0 column 0 to row 6 column 6 are accepted</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The game ends as expected when the user's torpedo count is less then the enemy ships remaining, resulting in mission failure</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The game ends as expected when the user's hull plates remaining reaches 0, resulting in mission failure</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The game ends as expected when the merchant ships remaining reaches 0, resulting in mission failure</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The game ends as expected when the enemy ships reaches 0, resulting in mission success</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>The mission failure narrative displays correctly</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>User can restart game successfully from mission failure narrative screen</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>User can exit program successfully from mission failure narrative screen</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>User can restart game successfully from mission success narrative screen</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->
<tr>
<td>User can exit program successfully from mission success narrative screen</td><td>:heavy_check_mark:</td>
</tr>
<!-- spacer -->


</table>

[Back to Manual Testing](#manual-testing)

<br>
<br>
<br>

</details>

<details>
  <summary><b>Code Validation</b></summary>
<br>
<!-- spacer -->
<details>
  <summary>  <i>Code Institute PEP8 Linter Validation</i></summary>
<br>

The python code passed through the [Code Institure PEP Linter](https://pep8ci.herokuapp.com/#) without returning any warnings or errors.

<br>
<table>
<tr><td><b>Code Institute Linter</b></td><td><b>Status</b></td></tr>

</tr>
<td>

![Python Validation](assets/documentation/code_validation.webp)

</td>
<td>
:heavy_check_mark:
</td>
</tr>
</table>
</details>


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
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_1_create_app.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 2: App setup page</i></summary>
<br>
Once the app is created, the setup page will be displayed. This page contains an overview of the data related to the app. From here, navigate to the 'Settings' tab.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_2_app_setup_page.webp)

</td>
</table>



</details>
<!-- spacer -->
<details>
  <summary><i> Step 3: Settings</i></summary>
<br>
On the Settings page, click on the 'Reveal Config Vars' button.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_3_settings.webp)

</td>
</table>




</details>
<!-- spacer -->
<details>
  <summary><i> Step 4: Config vars</i></summary>
<br>
In the Config Vars, add 'PORT' and '8000' in the fields as shown below. Then click 'Add'.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_4_config_vars.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 5: Add buildpacks</i></summary>
<br>
Once the Config Vars are added, the next step is to add two buildpacks to the app. Scroll down to the Buildpacks section and click on the 'Add buildpack' button.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_5_add_buildpacks.webp)

</td>
</table>


</details>
<!-- spacer -->
<details>
  <summary><i> Step 6: Add python buildpack</i></summary>
<br>
Select the python option from the menu, then click 'Add buildpack'. To note, it is important that the python buildpack is added first <b>before</b> any other buildpack!
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_6_add_python_buildpack.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 7: Add node.js buildpack</i></summary>
<br>
Once the python buildpack is added, select the node.js buildpack from the menu and click on the 'Add buildpack' button. To note, it is important that the node.js buildpack is added <b>after</b> the python buildpack!
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_7_add_nodejs_buildpack.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 8: Deploy screen</i></summary>
<br>
Once the buildpacks have been added (python, followed by node.js), navigate to the 'Deploy' tab.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_8_deploy_screen.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 9: Select Github</i></summary>
<br>
Select Github from the 'Deployment method' options.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_9_select_github.webp)

</td>
</table>


</details>
<!-- spacer -->
<details>
  <summary><i> Step 10: Enter repository name</i></summary>
<br>
Enter the repository name in the 'Connect to Github' field as shown below, then click on the 'Seach' button.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_10_enter_repository.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 11: Connect</i></summary>
<br>
Once the repository has been located, click on the 'Connect' button.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_11_click_connect.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 12: Connection confirmation</i></summary>
<br>
A confirmation will be displayed on the Github once the repository is connected to the Heroku app as shown below.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_12_connected_confirmation.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 13: Enable automatic deploys (optional)</i></summary>
<br>
Automatic deploys can be enabled if so desired by clicking on the 'Enable Automatic Deploys' button, this will result in the app being refreshed with updated code every time changes are pushed to Github. 
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_13_enable_auto_deploys.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 14: Manual deployment</i></summary>
<br>
The initial deployment of the app can be triggered by selecting 'main' from the 'Choose a branch to deploy' menu, then clicking on the 'Deploy Branch' button.
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_14_manual_deploy.webp)

</td>
</table>

</details>
<!-- spacer -->
<details>
  <summary><i> Step 15: Deployment confirmation</i></summary>
<br>
Once the app build and deployment has been completed in Heroku, a confirmation will be displayed as shown below. The app can now be viewed by clicking on the 'View' button.
<br>
<br>
The deployment process is now complete.
<br>
<br>
The live link to the app is https://battleship-rescue-4a195bb43cc9.herokuapp.com/
<br>
<br>
<table>
<tr>
<td>

![Create App](assets/documentation/deployment_15_deployment_confirmation.webp)

</td>
</table>

</details>
<!-- spacer -->
</details>

The live link to the app is https://battleship-rescue-4a195bb43cc9.herokuapp.com/

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




