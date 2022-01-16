const baseUrl = "https://website.ir";

const paramsContainer = "#params-container";
const queriesContainer = "#queries-container";
const paramBtn = "#param-submit";
const queryBtn = "#query-submit";
const generateBtn = "#generate";
const urlContainer = "#url-container";
const keyValueBox = ".keyValue-box";
const qInput = ".q-input";

const checkUrl = (url) => {
  cy.get(urlContainer).find("p").contains(url);
};

describe("URL Generator Sample Tests:", () => {
  beforeEach(() => {
    cy.visit("index.html");
  });
  it("Output should be correct #1", () => {
    const finalUrl = "https://website.ir/paramTestOne";
    cy.get(paramsContainer)
      .find(keyValueBox)
      .then(($el) => {
        $el.each((el) => {
          $el[el].querySelector(qInput).value = "paramTestOne";
        });
      });
    cy.get(generateBtn).click();
    checkUrl(finalUrl);
  });

  it("Output should be correct #2", () => {
    const finalUrl = "https://website.ir?queryTestOne=one";
    cy.get(queriesContainer)
      .find(keyValueBox)
      .then(($el) => {
        $el[0].querySelectorAll(qInput)[0].value = "queryTestOne";
        $el[0].querySelectorAll(qInput)[1].value = "one";
      });
    cy.get(generateBtn).click();
    checkUrl(finalUrl);
  });
});
