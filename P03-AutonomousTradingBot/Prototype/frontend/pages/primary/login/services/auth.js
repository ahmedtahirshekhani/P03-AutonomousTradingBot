// import bcrypt from 'bcrypt'
// const saltRounds = bcrypt.genSaltSync(10);

// const hashPassword = (password) => {
//     return bcrypt.hashSync(password, saltRounds);
// }


const login = (email, password, role) => {
    email = email.toLowerCase();
    // hashPassword = hashPassword(password);
    // console.log(hashPassword)
}

export {login}