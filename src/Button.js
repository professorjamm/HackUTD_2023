/* Author: Mohammad Zaaim Amin Rahman
 * Description: This file contains the code for the button components of the web application
 * Contains: Button Component: props
 */

const Button  = (props) => {

    return (
        <div className="button">
            <button onClick={props.callback}>{props.name}</button>
        </div>
    );

};

export default Button;