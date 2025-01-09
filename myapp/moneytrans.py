from web3 import Web3,HTTPProvider
blockchain_address="http://127.0.0.1:7545"
web3=Web3(HTTPProvider(blockchain_address))
if web3.isConnected():


    acc1="0x02410F6593852C6d3bba469646a2C87C5cF54990"
    acc2="0xe501C9DF632092815a3945fc7CcF299C1a17CaA1"

    prvkey="0xd09175def28bb9977981dfde318c5ab7a4dfff6526fccc9f5647f43806918c39"
    nonce= web3.eth.getTransactionCount(acc1)

    abcd = web3.eth.get_balance(acc1)
    abcd=web3.fromWei(abcd,'ether')
    print(abcd)



    tx={
        'nonce':nonce,
        'to':acc2,
        'value':web3.toWei(1,'ether'),
        'gas':200000,
        'gasPrice':web3.toWei('50','gwei')
    }
    signedtx=web3.eth.account.sign_transaction(tx,prvkey)
    hashx=web3.eth.send_raw_transaction(signedtx.rawTransaction)
    print(web3.toHex(hashx))