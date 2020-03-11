import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

const Header = props => {
    return (
        <View style={styles.headerContainer}>
            <Text style={styles.header}>{props.title}</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    headerContainer: {
        width: '100%',
        height: 90,
        paddingTop: 36,
        backgroundColor: '#5f6c11',
        alignItems: 'center',
        justifyContent: 'center'
    },
    header: {
        color: '#eae7e0',
        fontSize: 24
    }
});

export default Header;