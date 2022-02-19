Feature: I want to see the default vue 3 project webpage

    Scenario: Open the vue project default webpage successfully
    Given that I want to navigate to main page
    When I go to "http://localhost:8080"
    Then I will see the vue logo
    And I will see the following information
    | element | content                    |
    | h1      | Welcome to Your Vue.js App |
    | h3      | Installed CLI Plugins      |
    | h3      | Essential Links            |
    | h3      | Ecosystem                  |
    