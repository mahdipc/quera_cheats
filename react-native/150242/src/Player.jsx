import { View, Text, StyleSheet } from "react-native";

const Player = (props) => {
	return <View style={[style.player,props.isRed==true?style.red:style.blue]} >
		<Text style={style.text}>
		{props.name}
		</Text>
		<Text style={[style.text,style.goal]}>
		{props.goal}
		</Text>
		</View>;
};

const style = StyleSheet.create({
	red: {
		backgroundColor:"#cc0000"
	},
	blue: {
		backgroundColor:"#0000cc"
	},
	text: {
		color:"white",
		marginTop:50,
		textAlign:"center"
	},
	goal: {
		fontSize:50,
		fontStyle:"italic",
		fontWeight:"bold"
	},
	player: {
		flex: 1 ,
		width:350,
		maxWidth: "40%",
		height:600,
		maxHeight: "70%",
		borderWidth:5,
		borderColor:"#eebc1d",
		borderRadius:20,
		display: 'grid',
	},
});

export { style };

export default Player;
