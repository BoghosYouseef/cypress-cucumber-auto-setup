
# this is a simple script that automatically modifies the necessary files to make vue 3 work with cypress
# and cypress-cucumber-preprocessor

import json
import os

print("The dependency automation tool has started!")


def add_cypress_cucumber_preprocessor_json_dependency():
    """

    :param json_file_path: -> string: the absolute path to the input json file
    :return:
    """
    json_file_path = r"package.json"
    input_json_file = open(json_file_path, "r")

    # returns JSON object as
    # a dictionary
    input_json_file_in_dict_format = json.load(input_json_file)
    input_json_file.close()
    os.remove(json_file_path)

    input_json_file_in_dict_format["cypress-cucumber-preprocessor"] =  {"nonGlobalStepDefinitions": True,
                                             "stepDefinitions": "tests/e2e/specs",
                                                "commonPath": "tests/e2e/common",
                                                    "cucumberJson": {
                                                        "generate": True,
                                                        "outputFolder": "tests/e2e/cucumber-json",
                                                       "filePrefix": "",
                                                        "fileSuffix": ".cucumber"}
                                             }

    new_json_file = open("package.json", "a+")
    json.dump(input_json_file_in_dict_format, new_json_file)

    new_json_file.close()

    return


# Defines test file paths in the cypress.json file.
def add_cypress_cucumber_cypressjson_dependency():
    """

    :param json_file_path: -> string: the absolute path to the input json file
    :return:
    """

    json_file_path = r"cypress.json"
    os.remove(json_file_path)

    dependency = """
    {
        "pluginsFile": "tests/e2e/plugins/index.js",
        "baseUrl": "http://localhost:8080", 
        "chromeWebSecurity": false,
        "testFiles": "**/*.{feature,features}"
    }
        """

    new_json_file = open(json_file_path, "a+")
    new_json_file.write(dependency)
    new_json_file.close()

    return


def add_vue3_cucumber_dependency_inside_index_js():

    dependency = """/* eslint-disable arrow-body-style */
// https://docs.cypress.io/guides/guides/plugins-guide.html

// if you need a custom webpack configuration you can uncomment the following import
// and then use the `file:preprocessor` event
// as explained in the cypress docs
// https://docs.cypress.io/api/plugins/preprocessors-api.html#Examples

// /* eslint-disable import/no-extraneous-dependencies, global-require */
// const webpack = require('@cypress/webpack-preprocessor')

const cucumber = require('cypress-cucumber-preprocessor').default


module.exports = (on, config) => {
  // on('file:preprocessor', webpack({
  //  webpackOptions: require('@vue/cli-service/webpack.config'),
  //  watchOptions: {}
  // }))
  on("file:preprocessor", cucumber())
  return Object.assign({}, config, {
    fixturesFolder: "tests/e2e/fixtures",
    integrationFolder: "tests/e2e/specs",
    screenshotsFolder: "tests/e2e/screenshots",
    videosFolder: "tests/e2e/videos",
    supportFile: "tests/e2e/support/index.js",
  });
};"""

    path = "tests/e2e/plugins/index.js"
    os.remove(path)

    new_js_file = open(path, "a+")
    new_js_file.write(dependency)

    new_js_file.close()

    return


def create_a_feature_file_with_corresponding_cypress_test():
    path = "tests/e2e/specs/"
    feature_file_name = "featureFileTest"
    feature_file = open(path+feature_file_name+".feature", "a+")
    feature_file_content = """Feature: I want to see the default vue 3 project webpage

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
    """
    feature_file.write(feature_file_content)
    feature_file.close()

    os.mkdir(path+feature_file_name)
    cypress_test = open(path+feature_file_name+"/feature_file_test.spec.js", "a+")
    cypress_test_content = """Given('that I want to navigate to main page', () => {
 // step definitions can be empty! but that is not very useful
})
When('I go to "http://localhost:8080"', () => {
    cy.visit("/") // this just means go to the base page, which is http://localhost:8080 in this case.
})
Then('I will see the vue logo', () => {
    cy.get('img').should("be.visible")
})
And('I will see the following information', (datatable) => {
    
    rows = datatable.hashes()

    rows.forEach((row)=> {
        cy.get(row["element"])
            .contains(row["content"])
            .should("be.visible")
            .should("have.text",row["content"])
    })
    
})
    """
    cypress_test.write(cypress_test_content)
    cypress_test.close()

    return


if __name__ == '__main__':

    os.system("npm i cypress -D")
    os.system("npm install --save-dev cypress-cucumber-preprocessor")
    add_cypress_cucumber_preprocessor_json_dependency()
    add_cypress_cucumber_cypressjson_dependency()
    add_vue3_cucumber_dependency_inside_index_js()
    create_a_feature_file_with_corresponding_cypress_test()
    print("""Program finished! Check if everything is correct by running the following command in the console:
        \n npm run test:e2e \n
          """)
