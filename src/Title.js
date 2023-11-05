/* Author: Mohammad Zaaim Amin Rahman
 * Description: Holds the basic title object for the dynamic pages
 * Contains: Title component
 */

//Title Component: props= {title: string of the display title}
const Title = (props) => {

    return (
        <div className="title">
            <h1>{props.title}</h1>
        </div>
    );

};

export default Title;