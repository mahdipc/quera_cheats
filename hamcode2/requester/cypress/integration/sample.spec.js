describe("Sample Tests:", () => {
  it("sample", () => {
    cy.visit("index.html");
    cy.intercept("GET", "/hello", {
      statusCode: 200,
      body: {
        hello: "world",
      },
      delay: 50,
    }).as("hello");

    cy.intercept("GET", "/foo", {
      statusCode: 404,
      body: {
        foo: "bar",
      },
      delay: 50,
    }).as("foo");

    cy.get("#urls").type("/hello \n/foo");
    cy.get("#send-requests").click();
    cy.get("#results").children().should("have.length", "0");
    cy.wait("@hello");
    cy.get("#results").children().should("have.length", "1");
    cy.get("#results").children().eq(0).should("contain", "hello").and("contain", "world");

    cy.wait("@foo");
    cy.get("#results").children().should("have.length", "2");
    cy.get("#results").children().eq(1).should("have.text", "error")
  });
});
