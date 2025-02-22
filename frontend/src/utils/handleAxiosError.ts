import axios from "axios";
import { toast } from "react-toastify";

const handleAxiosError = (
  error: unknown,
  attemptedAction: string = "complete the request",
  unexpectedErrMessage: string = "An unexpected error occured",
): void => {
  // if FE error, note it's unexpected then toast & log
  if (!axios.isAxiosError(error)) {
    console.error(`${unexpectedErrMessage}:`, error);
    toast.error(`${unexpectedErrMessage}`);
    return;
  }

  // if BE error toast
  const baseErrMessage = `Failed to ${attemptedAction}`;
  toast.error(baseErrMessage);

  // if in dev env then console full BE error
  const serverMessage = error.response?.data?.message || "An error occured";
  if (import.meta.env.VITE_DEV)
    console.error(
      `${baseErrMessage}: ${serverMessage} ${
        error.response?.data || error.message
      }`,
    );
};

export default handleAxiosError;
