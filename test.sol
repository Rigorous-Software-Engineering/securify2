pragma solidity ^0.8.19;

contract HelloWorld {
    function my_simple_function() private pure returns (int res) {
        string memory hello = "hello world";

        return 5;
    }

    function my_middle_function() private pure returns (int res) {
        int my_variable = my_simple_function();
        return my_variable;
    }

    function a_complex_function() public returns (int res) {
        int result = my_middle_function();

        return result;
    }
}