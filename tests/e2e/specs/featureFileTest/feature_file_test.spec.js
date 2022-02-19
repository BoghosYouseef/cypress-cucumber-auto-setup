Given('that I want to navigate to main page', () => {
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
    