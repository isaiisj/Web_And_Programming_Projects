const sha256 = require('js-sha256');

class BlockChain{
  constructor(){
    this.dificulty = 4;
    this.chain = [this.createGenesisBlock()];
  }

  createGenesisBlock(){
    return new Block('', 'genesis block', new Date(), this.dificulty);
  }

  addNewBlock(transactions){
    const block = new Block(this.chain[this.chain.length - 1].hash, transactions, new Date(),this.dificulty);
    this.chain.push(block);
  }

  validateBlock(block){
     const hash = sha256(`${block.nonce}${block.previousBlock}${block.transactions}`);
    if(block.hash === hash) {
            console.log('valid block');
        } else {
            console.log('TEMPERED BLOCK');
        }
  }
}

class Block{
  constructor(previousBlock, transactions, timeStamp, dificulty){
    this.dificulty = dificulty;
    this.timeStamp = timeStamp;
    this.previousBlock = previousBlock;
    this.transactions = transactions;
    this.hash = '';
    this.nonce = this.createNonce();
  }

  createNonce(){
    let nonce = 0;
    const targetZeros = '0'.repeat(this.dificulty);
    
    while(true){
      const hash = sha256(`${nonce}${this.previousBlock}${this.transactions}${this.timeStamp}`);
      if(hash.startsWith(targetZeros)){
        this.hash = hash;
        break;
      }
      nonce++;
    }
    return nonce;
  }
}

const blockChain = new BlockChain();
blockChain.addNewBlock('new transactions');
blockChain.addNewBlock('new transactions 2');

/*const block1 = blockChain.chain[1];
block1.transactions = 'robar btc';

blockChain.validateBlock(block1);*/
console.log(blockChain);
