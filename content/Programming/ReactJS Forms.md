---
tags:
  - react
  - javascript
---
Using [[HTML Forms]] as [[ReactJS Component|Components]].
Because props are immutable, you need to use the onChange() function in react to change the value inside the form.
# Good Working Form
```js
import {useState} from 'react'

function Form() {
    const [value, setValue] = useState("");
    function handleChange(event){
        console.log(value);
        setValue(event.target.value);
    }
    return(
        <form>
            <input onChange={(e) => handleChange(e)} type="text" value={value}></input>
        </form>
    )
}
export default Form;
```