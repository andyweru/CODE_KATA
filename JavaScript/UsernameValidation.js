function validateUsr(username) {
    res =  /^[0-9a-z_]{4,16}$/.test(username)
    return res
  }