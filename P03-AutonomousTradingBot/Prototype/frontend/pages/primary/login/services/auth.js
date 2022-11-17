import axios from 'axios';
const apiproxy = "http://127.0.0.1:5000"
const analystLogin = (email, password) => {
    return new Promise((resolve, reject) => {
        // request content type json
        const req = {
            "email": email,
            "password": password
        }
        // convert req to json
        const jsonReq = JSON.stringify(req);
        axios.post('/api/analyst-login', jsonReq, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(res => {
                console.log(res);
                resolve(res.data);
            })
            .catch(err => {
                console.log(err);
                reject(err);
            });
    });
};

const investorLogin = (email, password) => {
    return new Promise((resolve, reject) => {
        axios.post('/api/investor/login', { email, password })
            .then(res => { 
                resolve(res.data);
            })
            .catch(err => {
                reject(err);
            });
    });
};


const login = (email, password, role) => {
    email = email.toLowerCase();
    if (role === 'analyst') {
        return analystLogin(email, password);
    }else if (role === 'admin') {
        return investorLogin(email, password);
    }else{
        return analystLogin(email, password);
    }
}

export {login}