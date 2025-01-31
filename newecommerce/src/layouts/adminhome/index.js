/**
=========================================================
* E-commerce MUI - v3.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-material-ui
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

import { useState } from "react";

// react-router-dom components
import { Link } from "react-router-dom";

// @mui material components
import Switch from "@mui/material/Switch";

// E-commerce MUI components
import ArgonBox from "components/ArgonBox";
import ArgonTypography from "components/ArgonTypography";
import ArgonInput from "components/ArgonInput";
import ArgonButton from "components/ArgonButton";
import preview from "../../../src/assets/images/browse.jpg";

// Authentication layout components
import IllustrationLayout from "layouts/authentication/components/IllustrationLayout1";

import axios from "axios";
import { ipofserver } from 'global';

// Image
const bgImage = ipofserver+'static/a.jpeg';

function Illustration() {
  const [rememberMe, setRememberMe] = useState(false);

  const handleSetRememberMe = () => setRememberMe(!rememberMe);

  const [inputField, setInputField] = useState({
    name: '',
    category: '',
    date: '',
    prize: '',
    description: '',
    instruction: ''
  })

  const inputsHandler = (e) => {
    const { name, value } = e.target;
    setInputField((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  }

  function clearInput() {
    setInputField({
      name: '',
      category: '',
      date: '',
      prize: '',
      description: '',
      instruction: ''
    });
    setFile(null);
    setSelectedFile('');
  }

  const [file, setFile] = useState();
  const [selectedFile, setSelectedFile] = useState();

  function handleChange(e) {
    console.log(e.target.files);
    setFile(URL.createObjectURL(e.target.files[0]));
    setSelectedFile(e.target.files[0]);
  }

  const handleSubmission = async () => {
    // console.log(isFilePicked);
    if (selectedFile == '' || inputField.name == '' || inputField.category == '' || inputField.date == '' || inputField.prize == '' || inputField.description == '' || inputField.instruction == '') {
      alert("Please fill all details !") // eslint-disable-line no-alert
    }
    else {

      const formData = new FormData();

      formData.append('File', selectedFile);
      formData.append('pname', inputField.name);
      formData.append('pcategory', inputField.category);
      formData.append('pdate', inputField.date);
      formData.append('pprize', inputField.prize);
      formData.append('description', inputField.description);
      formData.append('instruction', inputField.instruction);
      formData.append('user', 'admin');

      const res = await axios.post(`${ipofserver}addProduct`, formData);

      if (res.data == "success") {
        alert("Product added sucessfully !")
        clearInput()
      }
      else {
        alert("Product not uploaded !")
      }

    }
  };

  return (
    <IllustrationLayout
      title="Add product"
      description="Enter your product details"
      illustration={{
        image: bgImage,
        title: '"Attention is the new currency"',
        description:
          "The more effortless the writing looks, the more effort the writer actually put into the process.",
      }}
    >
      <ArgonBox component="form" role="form">
        <div className="App">
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 20 }}>
            <label htmlFor="file1">
              <img src={file == null ? preview : file} style={{
                width: 370, height: 270, borderWidth: 2, borderStyle: 'dashed', borderColor: 'black', borderRadius: 4
              }} />
            </label>
          </div>
          <input type="file" id="file1" onChange={handleChange} hidden />
        </div>
        <ArgonBox mb={2}>
          <ArgonInput type="text" placeholder="Product name" size="large" name="name" value={inputField.name}
            onChange={inputsHandler} />
        </ArgonBox>
        <ArgonBox mb={2}>
          <ArgonInput type="text" placeholder="Product category" size="large" name="category" value={inputField.category}
            onChange={inputsHandler} />
        </ArgonBox>
        <ArgonBox mb={2}>
          <ArgonInput type="date" placeholder="Product manufature date" size="large" name="date" value={inputField.date}
            onChange={inputsHandler} />
        </ArgonBox>
        <ArgonBox mb={2}>
          <ArgonInput type="number" placeholder="Product prize" size="large" name="prize" value={inputField.prize}
            onChange={inputsHandler} />
        </ArgonBox>
        <ArgonBox mb={2}>
          <ArgonInput type="text" placeholder="Product description" size="large" name="description" value={inputField.description}
            onChange={inputsHandler} />
        </ArgonBox>
        <ArgonBox mb={2}>
          <ArgonInput type="text" placeholder="How to use?" size="large" name="instruction" value={inputField.instruction}
            onChange={inputsHandler} />
        </ArgonBox>
        <ArgonBox display="flex" alignItems="center">
          <Switch checked={rememberMe} onChange={handleSetRememberMe} />
          <ArgonTypography
            variant="button"
            fontWeight="regular"
            onClick={handleSetRememberMe}
            sx={{ cursor: "pointer", userSelect: "none" }}
          >
            &nbsp;&nbsp;Remember me
          </ArgonTypography>
        </ArgonBox>
        <ArgonBox mt={4} mb={1}>
          <ArgonButton color="info" size="large" style={{ fontSize: 17 }} onClick={handleSubmission} fullWidth>
            Add product
          </ArgonButton>
        </ArgonBox>
      </ArgonBox>
    </IllustrationLayout>
  );
}

export default Illustration;
