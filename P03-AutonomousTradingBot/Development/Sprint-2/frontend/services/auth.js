import axios from "axios";

const login = (email, password) => {
  email = email.toLowerCase();
  return new Promise((resolve, reject) => {
    // request content type json
    const req = {
      email: email,
      password: password,
    };
    // convert req to json
    const jsonReq = JSON.stringify(req);
    console.log(jsonReq);

    axios
      .post(`/api/v1/auth/login`, jsonReq, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((res) => {
        localStorage.setItem("access_token", res.data.access_token);
        localStorage.setItem("expires_in", res.data.expires_in);
        localStorage.setItem("role", res.data.role);
        resolve(res);
      })
      .catch((err) => {
        console.log(err);
        reject(err);
      });
  });
};

const registerInvestor = async (ntn, inv_email, name, phone, address) => {
  var data = JSON.stringify({
    name: name,
    address: address,
    investor_email: inv_email,
    phone_number: phone,
    analyst_email: "",
    ntn: ntn,
  });

  var config = {
    method: "post",
    url: "/api/v1/register-investor",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      "Content-Type": "application/json",
    },
    data: data,
  };

  const response = await axios(config);
  return response.data;
};

const logout = () => {
  return new Promise((resolve, reject) => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("expires_in");
    localStorage.removeItem("role");

    axios
      .post(
        `/api/v1/logout`,
        {},
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("access_token")}`,
          },
        }
      )
      .then((res) => {
        resolve(res);
      })
      .catch((err) => {
        reject(err);
      });
  });
};

const getAllInvestors = async () => {
  var data = "";

  var config = {
    method: "get",
    url: "/api/v1/get-all-investors",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token")}`,
    },
    data: data,
  };

  const response = await axios(config);
  return response.data;
};

const getAllBots = async (investor_id) => {
  var data = JSON.stringify({
    investor_id: investor_id,
  });

  var config = {
    method: "post",
    url: "/api/v1/get-bots",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("access_token")}`,
    },
    data: data,
  };

  const response = await axios(config);
  return response.data;
};

const addBot = async (investor_id, risk_appetite, target_return, amount, duration) => {
	var data = JSON.stringify({
		investor_id: investor_id,
		trades: [],
		assigned_model: 0,
		risk_appetite: risk_appetite,
		target_return: target_return,
		duration: '10-12-2023',
		amount:amount
	});

	var config = {
		method: 'post',
		url: '/api/v1/add-bot',
		headers: {
			Authorization: `Bearer ${localStorage.getItem('access_token')}`,
			'Content-Type': 'application/json',
		},
		data: data,
	};

	const response = await axios(config);
	return response.data;}


const initiateBotExecution = async (bot_id) => {
  var data = JSON.stringify({
    bot_id: bot_id,
  });

  var config = {
    method: "put",
    url: "/api/v1/initiate-bot-execution",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      "Content-Type": "application/json",
    },
    data: data,
  };

  const response = await axios(config);
  console.log(response.data);
  return response.data;
};

const terminateBot = async (bot_id) => {
  var data = JSON.stringify({
    bot_id: bot_id,
  });

  var config = {
    method: "put",
    url: "/api/v1/terminate-bot",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      "Content-Type": "application/json",
    },
    data: data,
  };

  const response = await axios(config);
  console.log(response.data);
  return response.data;
};

export {
  login,
  registerInvestor,
  logout,
  getAllInvestors,
  getAllBots,
  addBot,
  initiateBotExecution,
  terminateBot,
};
