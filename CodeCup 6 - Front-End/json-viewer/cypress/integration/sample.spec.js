const textArea = "#textarea";
const submitBtn = "#submit-btn";

describe("Json Viewer Sample Tests:", () => {
  beforeEach(() => {
    cy.visit("index.html");
  });
  it("click on submit button and render curly braces ({}) of json", () => {
    let jsonTest = {
      test: "sample",
    };
    cy.get(textArea).type(JSON.stringify(jsonTest), {
      parseSpecialCharSequences: false,
      delay: 0,
    });
    cy.get(submitBtn).click();
    cy.get("#result > ul > li > .json-viewer-object-end").should(
      "have.text",
      "}"
    );
    cy.get("#result > ul > li > .json-viewer-object-start").should(
      "have.text",
      "{"
    );
  });
});
