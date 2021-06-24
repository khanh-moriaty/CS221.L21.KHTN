const timeStamp2str = timeStamp => {
    const tsd = new Date(timeStamp);
    return tsd.toLocaleString();
}
  
export default timeStamp2str;