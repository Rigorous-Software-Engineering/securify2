pragma solidity ^0.8.19;

contract HelloWorld {
    function my_function() private pure returns (int res) {
        int my_variable = 5;
        return my_variable;
    }

    function a_complex_function() public returns (int res) {
        int result = my_function();

        return result;
    }
}