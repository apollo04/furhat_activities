import { AxiosError, AxiosResponse } from 'axios';
import { UseMutationResult, useMutation } from 'react-query';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useSubmitFeedback(): UseMutationResult<
  AxiosResponse<any>,
  AxiosError<{ message: string }>,
  any
> {
  const postSubmitFeedback = (payload: any) => {
    return axiosUnauthorizedInstance.post(`submit_feedback`, payload);
  };

  return useMutation(postSubmitFeedback);
}
