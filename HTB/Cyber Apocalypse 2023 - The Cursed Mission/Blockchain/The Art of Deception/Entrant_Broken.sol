pragma solidity ^0.8.18;


interface HighSecurityGate {
    function enter() external;
}

contract Entrant {

    uint8 public _myVar;
    event MyEvent(uint indexed _var);
    string public _myString;
    address gateAddr;

    function setVar(uint8 _var) public {
        _myVar = _var;
        emit MyEvent(_var);
    }
    
    function name() external returns (string memory) {
        return "Nova";
    }

    function getVar() public view returns (uint8) {
        return _myVar;
    }
    
    
    function setGateAddr(address _gate) public payable {
       gateAddr = _gate;
    }
    
    
    
    function enter() external {
        HighSecurityGate(gateAddr).enter();
    }

}