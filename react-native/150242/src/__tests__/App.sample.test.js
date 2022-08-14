import { style as playerStyle } from "../Player.jsx";
import { StyleSheet } from "react-native";
test("Player style.red", () => {
	const styles = StyleSheet.flatten(playerStyle.red);
	expect(styles.backgroundColor.toLowerCase() === "#cc0000").toBe(true);
});

test("Player style.blue", () => {
	const styles = StyleSheet.flatten(playerStyle.blue);
	expect(styles.backgroundColor.toLowerCase() === "#0000cc").toBe(true);
});
