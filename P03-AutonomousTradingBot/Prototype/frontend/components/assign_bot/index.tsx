const AssignBot = ({name, email, phone} : {name: string , email: string, phone: string}) => {
    return (
        <tr className="hover">
                  <th className="text-primary">1</th>
                  <td>{name}</td>
                  {/* <td>ganderton@gmail.com</td> */}
                  <td>{email}</td>
                  <td>{phone}</td>
                  <td>
                    <div className="dropdown dropdown-right ">
                      <label tabIndex={0} className="btn m-1 bg-black">
                        Assign
                      </label>
                      <ul
                        tabIndex={0}
                        className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
                      >
                        <li>
                          <div className="form-control  max-w-xs bg-black">
                            <label className="label">
                              <span className="label-text">
                                Enter Number of Bots
                              </span>
                            </label>
                            <input
                              type="number"
                              placeholder="Num"
                              className="input input-bordered w-full max-w-xs"
                            />
                            <label className="label">
                            <button className="btn btn-primary">Enter</button>
                            </label>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </td>
                </tr>
    )
}

export default AssignBot