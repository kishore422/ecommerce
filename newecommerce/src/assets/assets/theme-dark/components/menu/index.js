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

// E-commerce MUI base styles
import boxShadows from "assets/theme-dark/base/boxShadows";
import typography from "assets/theme-dark/base/typography";
import colors from "assets/theme-dark/base/colors";
import borders from "assets/theme-dark/base/borders";

// E-commerce MUI helper functions
import pxToRem from "assets/theme-dark/functions/pxToRem";

const { lg } = boxShadows;
const { size } = typography;
const { text, background } = colors;
const { borderRadius } = borders;

const menu = {
  defaultProps: {
    disableAutoFocusItem: true,
  },

  styleOverrides: {
    paper: {
      minWidth: pxToRem(160),
      boxShadow: lg,
      padding: `${pxToRem(16)} ${pxToRem(8)}`,
      fontSize: size.sm,
      color: text.main,
      textAlign: "left",
      backgroundColor: `${background.dark} !important`,
      borderRadius: borderRadius.md,
    },
  },
};

export default menu;
