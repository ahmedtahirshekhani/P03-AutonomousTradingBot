import axios from "axios";
import { useRouter } from "next/router";
const apiproxy = "http://127.0.0.1:5000";
const loginAuth = (email, password, role) => {
	return new Promise((resolve, reject) => {
		// request content type json
		const req = {
			email: email,
			password: password,
		};
		// convert req to json
		const jsonReq = JSON.stringify(req);
		result = {};
		axios
			.post(`/api/${role}-login`, jsonReq, {
				headers: {
					"Content-Type": "application/json",
				},
			})
			.then((res) => {
				console.log(res);
				localStorage.setItem("token", res.data.token);
				localStorage.setItem("expiry", res.data.expiry);
				localStorage.setItem("role", role);
				resolve(res);
			})
			.catch((err) => {
				console.log(err);
				reject(err);
			});
	});
};

const login = (email, password, role) => {
	email = email.toLowerCase();
	return loginAuth(email, password, role);
};

const registerInvestor = (
	ntn,
	inv_email,
	analyst_email,
	name,
	phone,
	address
) => {
	const req = {
		investor_email: inv_email,
		name: name,
		phone_number: phone,
		analyst_email: analyst_email,
		address: address,
		ntn: ntn,
	};
	const jsonReq = JSON.stringify(req);
	return new Promise((resolve, reject) => {
		axios
			.post("/api/register-investor", jsonReq, {
				headers: {
					"Content-Type": "application/json",
				},
			})
			.then((res) => {
				resolve(res.data);
			})
			.catch((err) => {
				reject(err);
			});
	});
};

const logout = (email, role) => {
	const emailReq = {
		email: email,
	};
	const jsonReq = JSON.stringify(emailReq);
	return new Promise((resolve, reject) => {
		axios
			.post(`/api/${role}-logout`, jsonReq, {
				headers: {
					"Content-Type": "application/json",
				},
			})

			.then((res) => {
				localStorage.removeItem("token");
				localStorage.removeItem("expiry");
				localStorage.removeItem("role");
				resolve(res);
			})
			.catch((err) => {
				reject(err);
			});
	});
};

export { login, registerInvestor, logout };
