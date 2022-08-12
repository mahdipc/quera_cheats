import App from "../../App.js";

import { render, screen } from "@testing-library/react-native";

test("Initial Number", () => {
	render(<App />);
	screen.getByText("0");
});
