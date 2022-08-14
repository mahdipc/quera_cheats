import React from "react";
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

import Row from "./src/Row.jsx";
import Player from "./src/Player.jsx";

export default function App() {
	return (
		<View>
			<Text style={style.header}>FIFA 22 Quera</Text>
			<Row>
				<Player name="Mahyar" goal={5} isRed />
				<Player name="Salib" goal={3} />
			</Row>
			<StatusBar style="auto" />
		</View>
	);
}

const style = StyleSheet.create({
	header: {
		fontSize: 50,
		fontStyle: "italic",
		fontWeight: "bold",
		textAlign: "center",
	},
});
