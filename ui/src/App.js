import "./App.css";
import { AuthProvider } from "./provider/useAuth";
import { BrowserRouter } from "react-router-dom";
import { AppRoutes } from "./routes/Routes";
import ResponsiveAppBar from "./features/Navigation/navbar";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

// function InnerApp() {
//     const { user, loading, error, login, signUp, logout } = useAuth();
// }

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <ThemeProvider theme={darkTheme}>
          <CssBaseline>
            <ResponsiveAppBar />
            <BrowserRouter>
              <AppRoutes />
            </BrowserRouter>
          </CssBaseline>
        </ThemeProvider>
      </AuthProvider>
    </div>
  );
}

export default App;
