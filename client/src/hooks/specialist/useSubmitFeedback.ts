import { AxiosError, AxiosResponse } from 'axios';
import { UseMutationResult, useMutation } from 'react-query';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useSubmitFeedback(
  child_id: string,
): UseMutationResult<AxiosResponse<any>, AxiosError<{ message: string }>, any> {
  const postSubmitFeedback = (payload: any) => {
    return axiosUnauthorizedInstance.post(
      `children/${child_id}/add_feedback/`,
      payload,
    );
  };

  return useMutation(postSubmitFeedback);
}
