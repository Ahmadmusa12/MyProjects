import React, { useState } from 'react';
import { View, Text, TextInput, StyleSheet, SafeAreaView } from 'react-native';

export default function App() {
  const [miles, setMiles] = useState('');
  const [kilometers, setKilometers] = useState('');

  const handleMilesChange = (value) => {
    setMiles(value);
    const km = parseFloat(value) * 1.60934;
    setKilometers(value ? km.toFixed(2) : '');
  };

  const handleKilometersChange = (value) => {
    setKilometers(value);
    const mi = parseFloat(value) / 1.60934;
    setMiles(value ? mi.toFixed(2) : '');
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Mileage Converter</Text>

      <Text style={styles.label}>Miles:</Text>
      <TextInput
        style={styles.input}
        keyboardType="numeric"
        value={miles}
        onChangeText={handleMilesChange}
        placeholder="Enter miles"
      />

      <Text style={styles.label}>Kilometers:</Text>
      <TextInput
        style={styles.input}
        keyboardType="numeric"
        value={kilometers}
        onChangeText={handleKilometersChange}
        placeholder="Enter kilometers"
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fefefe',
    padding: 20,
    justifyContent: 'center',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 40,
  },
  label: {
    fontSize: 18,
    marginBottom: 8,
    color: '#333',
  },
  input: {
    height: 50,
    borderColor: '#aaa',
    borderWidth: 1,
    paddingHorizontal: 12,
    borderRadius: 8,
    fontSize: 18,
    marginBottom: 24,
  },
});
Command + S

