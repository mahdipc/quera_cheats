import { View, StyleSheet } from "react-native";

const Row = ({children}) => <View style={style.row}> {children}</View>;

const style = StyleSheet.create({
	row: {
		flex:1,
			flexDirection: "row",
			justifyContent:"space-around",
			alignItems: "center",
			minHeight: "50%",
			maxHeight: "100%",
			maxWidth:"100%",
			minWidth: "80%",
			marginTop:50,
			alignSelf: "center",
		},
});

export { style };
export default Row;
