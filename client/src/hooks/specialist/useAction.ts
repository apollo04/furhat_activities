import { AxiosError, AxiosResponse } from 'axios';
import { useMutation, UseMutationResult } from 'react-query';
import { axiosUnauthorizedInstance } from 'utils/request';

export default function useAction(
  category: string,
  action: string,
  ip: string,
): UseMutationResult<AxiosResponse<any>, AxiosError<{ message: string }>, any> {
  const runAction = () => {
    return axiosUnauthorizedInstance.get(
      `/categories/${category}/actions/${action}?ip=${ip}`,
      {},
    );
  };

  return useMutation(runAction);
}
