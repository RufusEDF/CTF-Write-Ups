pragma solidity ^0.8.18;


interface HighSecurityGate {
    function enter() external;
}

contract StoreVar {

    uint8 public _myVar;
    event MyEvent(uint indexed _var);
    string public _myString;
    address entrantAddr;
    string public flag;

    function setVar(uint8 _var) public {
        _myVar = _var;
        emit MyEvent(_var);
    }

    function getVar() public view returns (uint8) {
        return _myVar;
    }
    
   
    function setEntrantAddr(address _entrant) public payable {
       entrantAddr = _entrant;
    }
    
    function setFlag(string memory _flag) public {
       flag = _flag;
    }
    

   
    function enter() external {
        HighSecurityGate(entrantAddr).enter();
    }
    
    function name() external returns (string memory) {
        setFlag("Fl4G");
        if (_myVar != 2) {
            setVar(2);
            return "Nova";
        } else if (_myVar == 2) { 
            return "Pandora";
        }
    }

}