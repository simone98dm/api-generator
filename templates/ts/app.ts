import express from "express";
import cors from "cors";
import bodyParser from "body-parser";
import morgan from "morgan";
//project-imports
import { port, prefix } from "./src/configs/api.config";

const server = express();
server.use(cors());
server.use(bodyParser.json());
server.use(morgan("dev"));
//defile-routes

server.listen(port, () =>
  console.log("API-ENDPOINT are running (:" + port + ")")
);
