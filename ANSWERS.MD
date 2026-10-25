
# Teorifrågor
Svara kortfattat på följande frågor i ANSWERS.md för att demonstrera dina kunskaper.
1.	Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
    * Enhetstest: Testar en enskild liten del (t.ex. en funktion eller klass) isolerat, ofta med mockar. Snabbt och många.

    * Integrationstest: Testar att flera delar fungerar tillsammans (t.ex. API mot databas, frontend mot backend).

    * Regressionstest: Testar att befintlig funktionalitet fortfarande fungerar efter ändringar – för att upptäcka att man inte brutit något.

    * Prestandatest: Mäter hastighet, svarstider, belastning och skalbarhet (t.ex. lasttest, stresstest).


2.	Beskriv hur det går till när man arbetar med TDD.

    Man arbetar i en kort cykel (red–green–refactor):

    * Red: Skriv ett test som beskriver önskad funktionalitet – det misslyckas eftersom koden inte finns.

    * Green: Skriv minsta möjliga kod för att testet ska gå igenom.

    * Refactor: Förbättra koden utan att ändra beteendet, kör testerna igen.

    Cykeln upprepas i små steg, vilket ger tät testtäckning och en design som drivs av tester.


3.	Beskriv hur BDD skiljer sig från TDD.

    * TDD fokuserar på hur koden är uppbyggd – tester på enhetsnivå som driver implementationen.

    * BDD (Behavior-Driven Development) fokuserar på beteende ur användarens/systemets perspektiv, ofta med ett gemensamt språk (Given–When–Then) som är läsbart för både utvecklare och affärssidan. BDD-tester är ofta mer på integrations-/acceptansnivå och beskriver scenarier snarare än tekniska detaljer.

    * Kort: TDD = utvecklardrivet, kodnära; BDD = beteendedrivet, verksamhetsnära.


4.	Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.

    Förutsättningslöst skulle jag välja en testpyramid med:

    * Enhetstester (backend): Affärslogik som lånelistor, statusberäkningar, validering – snabba och isolerade.

    * Enhetstester/komponenttester (frontend): Enskilda React-komponenter (t.ex. en bokrad, formulär) med t.ex. Testing Library.

    * Integrationstester (backend): API-endpoints mot en testdatabas – verifierar routing, validering och databasanrop tillsammans.

    * Integrationstester/E2E (frontend↔backend): Kritiska användarflöden som "lägg till bok i läslistan" och "markera som läst", t.ex. med Playwright/Cypress.

    * Regressionstester: CI-körning av hela sviten vid varje ändring för att skydda befintlig funktionalitet.

    * Prestandatest: Enklare lasttest på API:et (t.ex. k6) för att säkerställa rimliga svarstider.

    * Tillgänglighetstester: Automatiserad a11y-kontroll (axe) eftersom det är en publik webbsida.

    Motivering: Testpyramiden ger snabb återkoppling (många enhetstester), realistisk verifiering (integration/E2E för kritiska flöden) och skydd mot regressioner. E2E-tester hålls få eftersom de är långsamma och sköra, medan enhets- och integrationstester täcker merparten.
