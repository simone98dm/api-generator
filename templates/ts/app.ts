import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import morgan from "morgan";
//project-imports
import * as REPLACEMERoutes from "./src/routes/REPLACEME.route";
import { port, prefix } from "./src/configs/api.config";

const server = express();
server.use(cors());
server.use(bodyParser.json());
server.use(morgan("dev"));
//defile-routes
server.use(prefix, REPLACEMERoutes.router);

server.listen(port, () =>
  console.log("API-ENDPOINT are running (:" + port + ")")
);
