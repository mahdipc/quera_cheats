import React, { useState } from 'react'
import { StatusBar } from 'expo-status-bar'
import { StyleSheet, Text, View, Button } from 'react-native'

export default function App() {
  const [count, setCount] = useState(0)
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Quera Counter App</Text>
      <Text style={styles.counter}>{count}</Text>
      <View style={styles.btnContainer}>
        <Button
          onPress={() => {
            setCount(count + 1)
          }}
          title={'+'}
          color="#00dd00"
        />
        <Button
          onPress={() => {
            count > 0 ? setCount(count - 1) : 0
          }}
          title={'-'}
          color="#dd0000"
        />
      </View>
      <StatusBar style="auto" />
    </View>
  )
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  header: {
    fontSize: 32,
    fontStyle: 'italic',
    fontWeight: 'bold',
    position: 'absolute',
    top: 200,
  },
  counter: {
    fontSize: 16,
  },
  btnContainer: {
    margin: 30,
    width: 200,
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
})
