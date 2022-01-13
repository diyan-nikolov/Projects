// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract SimpleStorage {

    // this will get initialized to 0
    uint256 public favoriteNumber;
    bool favoriteBool;

    // struct are ways to define create new types objects in Solidity 
    struct People {
        uint256 favoriteNumber;
        string name;
    } 
    //creating a list of objects (array)
    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store (uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    //view, pure (does computations)
    function retrieve() public view returns(uint256) {
        return favoriteNumber;
    } 

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
