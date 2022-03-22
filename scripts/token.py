#!/usr/bin/python3

from brownie import Token, accounts


def main():
    print("Token.sol ContractContainer: ", Token, " \n Deploying Token...")
    # Token constructor arguments: name, symbol, decimals, initialSupply
    t = Token.deploy("Test Token2", "TST2", 18, 1e21, {"from": accounts[0]})
    print("Token Contract object created")

    # Code below should be done in test folder
    print("Token of account[0]: ", t.balanceOf(accounts[0]))
    print("Token of account[1]: ", t.balanceOf(accounts[1]))
    print("Token transfer parameters: ", t.transfer.info())
    tx = t.transfer(accounts[1], 1e20, {"from": accounts[0]})
    print("Token transfer: ", tx.events["Transfer"])
    print("Transfer call trace: ", tx.call_trace())
    print("Token of account[1]: ", t.balanceOf(accounts[1]))
    print("Transfer from account[2] to account[1]")
    tx2 = t.transfer(accounts[1], 1e20, {"from": accounts[2]})
    print("Transfer traceback: ", tx2.traceback())
